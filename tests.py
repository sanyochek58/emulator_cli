import pytest
import os
from commands import CommandExecutor

@pytest.fixture(scope="module")
def setup_vfs():
    vfs_dir = "test_vfs"
    os.mkdir(vfs_dir)
    with open(os.path.join(vfs_dir, "test.txt"), "w") as f:
        f.write("Hello World!\nThis is a test file.")
    yield vfs_dir
    # Удаление файлов после тестов
    for root, dirs, files in os.walk(vfs_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(vfs_dir)

def test_ls(setup_vfs):
    executor = CommandExecutor(setup_vfs)
    result = executor.ls(".")
    assert "test.txt" in result

def test_du(setup_vfs):
    executor = CommandExecutor(setup_vfs)
    result = executor.du(".")
    assert result is not None
    assert "Total size" in result
    assert int(result.split()[2]) > 0

def test_wc(setup_vfs):
    executor = CommandExecutor(setup_vfs)
    result = executor.wc("test.txt")
    assert "Lines: 2" in result
    assert "Words: 7" in result
    assert "Bytes" in result

def test_chown(setup_vfs):
    executor = CommandExecutor(setup_vfs)
    result = executor.chown("new_user", "test.txt")
    assert "Changed owner of test.txt to new_user" in result