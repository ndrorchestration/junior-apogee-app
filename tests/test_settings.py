from junior_apogee_app.settings import Settings


def test_default_settings():
    s = Settings()
    assert s.environment in ("development", "staging", "production")


def test_env_file(tmp_path, monkeypatch):
    # create a temporary .env file
    env_file = tmp_path / ".env"
    env_file.write_text("API_KEY=abc123\nENVIRONMENT=production\n")
    monkeypatch.chdir(tmp_path)
    s = Settings()
    assert s.api_key == "abc123"
    assert s.environment == "production"
