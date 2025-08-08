class Solution:
    def simplifyPath(self, path: str) -> str:
        #mapping = {"..":"/", "//":"/"}
        stack = []
        path = path.split("/")
        for pth in path:
            if pth == "" or pth == ".":
                continue
            elif pth == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(pth)

        return "/"+"/".join(stack)