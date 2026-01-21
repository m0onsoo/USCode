class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split("/")

        path = []
        for f in files:
            if f == ".." and path:
                # 상위 경로가 존재할때만
                path.pop()
            elif f == ".." or f == ".":
                # 그 외에는 스킵
                continue
            elif len(f) > 0:
                path.append(f)

        result = "/".join(path)
  

        return "/" + result