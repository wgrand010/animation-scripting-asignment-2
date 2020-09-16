from pathlib import Path


class SceneFile(object):

    def __init__(self, path):
        self.folder_path = Path()
        self.descriptor = 'main'
        self.task = None
        self.ver = 1
        self.ext = '.ma'
        self._init_from_path(path)

    @property
    def filename(self):
        pattern = "{descriptor}_{task}_v{ver:03d}{ext}"
        return pattern.format(descriptor=self.descriptor,
                              task=self.task,
                              ver=self.ver,
                              ext=self.ext)

    @property
    def path(self):
        return self.folder_path / self.filename

    def _init_from_path(self, path):
        path = Path(path)
        self.folder_path = path.parent
        self.ext = path.suffix
        self.descriptor, self.task, ver = path.stem.split("_")
        self.ver - int(ver.split("v")[-1])


scene_file = SceneFile("D:/tank_model_v001.ma")
print(scene_file.path)
print(scene_file.filename)
