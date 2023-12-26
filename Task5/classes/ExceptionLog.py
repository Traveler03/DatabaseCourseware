class ExceptionLog:
    def __init__(self, monitor_id, exception_detail):
        self._monitor_id = monitor_id
        self._exception_detail = exception_detail

    @property
    def monitor_id(self):
        return self._monitor_id

    @monitor_id.setter
    def monitor_id(self, monitor_id):
        self._monitor_id = monitor_id

    @property
    def exception_detail(self):
        return self._exception_detail

    @exception_detail.setter
    def exception_detail(self, exception_detail):
        self._exception_detail = exception_detail




