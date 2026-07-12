class Solution:
    def secondsBetweenTimes(self, start: str, end: str) -> int:
        st_hr,st_min,st_sec=map(int,start.split(":"))
        e_hr,e_min,e_sec=map(int,end.split(":"))

        sr_time=(st_hr*3600) + (st_min*60) + (st_sec)
        e_time=(e_hr*3600) + (e_min*60) + (e_sec)

        return e_time-sr_time