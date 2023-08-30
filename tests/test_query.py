from voicevox_python import Client, AudioQuery


def test_audio_query():
    client = Client()
    query = client.create_audio_query("こんにちは", 0)
    assert isinstance(query, AudioQuery)


def test_synthesis():
    client = Client()
    query = client.create_audio_query("こんにちは", 0)
    audio = client.synthesis(query, 0)
    assert isinstance(audio, bytes)


def test_multi_synthesis():
    client = Client()
    query = client.create_audio_query("こんにちは", 0)
    audio = client.multi_synthesis([query], 0)
    with open("test.zip", "wb") as f:
        f.write(audio)
    assert isinstance(audio, bytes)
