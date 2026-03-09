from junior_apogee_app.metrics_backends import get_backend, register_backend, MemoryBackend


def test_memory_backend():
    mb = MemoryBackend()
    mb.record("x", 1)
    assert mb.storage["x"] == 1


def test_register_and_get():
    class Dummy:
        def record(self, name, value):
            pass

    register_backend("dummy", Dummy())
    assert isinstance(get_backend("dummy"), Dummy)
