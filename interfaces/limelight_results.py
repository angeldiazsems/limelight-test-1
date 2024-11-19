class limelightResults:
    tagId: int

    def __init__(self, data: dict) -> None:
        self.tagId = data["Fiducial"][0]["fID"]