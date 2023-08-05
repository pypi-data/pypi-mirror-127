import chily
import os
from hashlib import sha256
from .proto.length_delimited import serialize_length_delimited
from .proto.delta_enclave_api_pb2 import ChunkHeader, EncryptionHeader, VersionHeader
from typing import BinaryIO, Iterator, Tuple, Optional
from io import TextIOWrapper

__all__ = ["Key"]

KEY_LEN = 32

class Key():
    """
    This class wraps the key material that is used to encrypt the
    files that are uploaded to the decentriq platform
    """
    material: bytes

    def __init__(self, material: Optional[bytes] = None):
        """
        Returns a new `Key` instance, can optional specify the raw key material
        """
        if material == None:
            key_bytes = os.urandom(KEY_LEN)
        else:
            if len(material) != KEY_LEN:
                raise Exception("Invalid key length, must be 32 bytes")
            key_bytes = material
        self.material = key_bytes

def create_chunk_header(extra_entropy: bytes) -> bytes:
    chunk_header = ChunkHeader()
    chunk_header.extraEntropy = extra_entropy

    chunk_header_bytes = serialize_length_delimited(chunk_header)
    return chunk_header_bytes


def create_version_header() -> bytes:
    version_header = VersionHeader()
    version_header.version = 0
    return serialize_length_delimited(version_header)

# Returns (integrity hash, encrypted blob)
def create_encrypted_chunk(
        key: bytes,
        extra_entropy: bytes,
        data: bytes
) -> Tuple[bytes, bytes]:
    chunk_bytes = []

    version_header = create_version_header()
    chunk_bytes.append(version_header)

    chunk_header = create_chunk_header(extra_entropy)
    chunk_bytes.append(chunk_header)

    chunk_bytes.append(data)

    chunk = b''.join(chunk_bytes)
    chunk_hasher = sha256()
    chunk_hasher.update(chunk)
    chunk_hash = chunk_hasher.digest()

    cipher = StorageCipher(key)
    encrypted_chunk = cipher.encrypt(chunk)

    return chunk_hash, encrypted_chunk

class CsvChunker(Iterator):
    def __init__(self, input_stream: BinaryIO, chunk_size: int):
        self.chunk_size = chunk_size
        self.input_stream = TextIOWrapper(input_stream)
        self.beginning_stream_offset = input_stream.tell()

    def reset(self):
        self.input_stream.seek(self.beginning_stream_offset)

    def __iter__(self) -> Iterator[Tuple[bytes, bytes]]:
        self.reset()
        return self

    # returns (hash, chunk)
    def __next__(self) -> Tuple[bytes, bytes]:
        version_header_bytes = create_version_header()
        chunk_header_bytes = create_chunk_header(os.urandom(16))

        # Does not account for header size
        current_chunk_size = 0
        starting_offset = self.input_stream.tell()
        chunk_bytes = [version_header_bytes, chunk_header_bytes]

        line = self.input_stream.readline()
        
        while line:
            line_bytes = line.encode("utf-8")
            current_chunk_size = self.input_stream.tell() - starting_offset
            chunk_bytes.append(line_bytes)
            if current_chunk_size > self.chunk_size:
                break
            line = self.input_stream.readline()
        else:
            if current_chunk_size == 0:
                raise StopIteration

        chunk = b''.join(chunk_bytes)
        chunk_hasher = sha256()
        chunk_hasher.update(chunk)
        chunk_hash = chunk_hasher.digest()
        return chunk_hash, chunk


class StorageCipher():
    def __init__(self, symmetric_key: bytes):
        self.enc_key = symmetric_key
        self.cipher: chily.Cipher = chily.Cipher.from_symmetric(self.enc_key)

    def encrypt(self, data: bytes) -> bytes:
        nonce = chily.Nonce.from_random()
        encrypted_data = self.cipher.encrypt(data, nonce)

        encryption_header = EncryptionHeader()
        encryption_header.chilyKey.encryptionNonce = bytes(nonce.bytes)

        serialized_encryption_header = serialize_length_delimited(encryption_header)
        encrypted_data_with_header = bytes(list(serialized_encryption_header) + encrypted_data)
        return encrypted_data_with_header
