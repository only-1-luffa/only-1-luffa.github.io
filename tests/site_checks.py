from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BLOG = SITE / "blog" / "gps-gaussian-plus-camera-views.html"
INDEX = SITE / "index.html"
STYLE = SITE / "styles" / "main.css"
REPORT = ROOT / "report" / "homework-report.md"
AVATAR = SITE / "assets" / "images" / "avatar.png"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    required_files = [INDEX, BLOG, STYLE, SITE / "AGENTS.md", REPORT, AVATAR]
    for path in required_files:
        require(path.exists(), f"Missing required file: {path.relative_to(ROOT)}")

    index = read_text(INDEX)
    blog = read_text(BLOG)
    style = read_text(STYLE)
    report = read_text(REPORT)

    require("高司晨" in index, "Homepage must include the public name.")
    require("藤上的丝瓜" in index, "Homepage must include the nickname.")
    require('<a class="brand" href="index.html">高司晨</a>' in index, "Top-left brand must be Gao Sichen.")
    require("assets/images/avatar.png" in index, "Homepage must reference the profile avatar.")
    require("profile-card" in index, "Homepage must use the avatar profile card.")
    require("<h1>高司晨</h1>" not in index, "Homepage should not open with a giant repeated name.")
    require("https://github.com/only-1-luffa" in index, "Homepage must link to GitHub profile.")
    require("blog/gps-gaussian-plus-camera-views.html" in index, "Homepage must link to the blog page.")
    require('href="../index.html"' in blog or "href='../index.html'" in blog, "Blog page must link back to homepage.")
    require("GPS-Gaussian+" in blog, "Blog must discuss GPS-Gaussian+.")
    require("固定机位" in blog, "Blog must discuss fixed camera positions.")
    require("实时三维直播" in blog, "Blog must discuss real-time 3D streaming.")
    require("已有的相机系统" in blog and "官方" in blog and "不匹配" in blog, "Blog must describe the current camera-system mismatch problem.")
    require("进一步优化算法" in blog, "Blog must mention the need for further algorithm optimization.")
    require("@media" in style, "Stylesheet must include responsive CSS.")
    require("AI Agent" in report, "Report must include AI Agent usage notes.")

    public_pages = index + "\n" + blog
    unresolved = re.findall(r"TODO|TBD|待补充|PLACEHOLDER", public_pages, flags=re.IGNORECASE)
    require(not unresolved, f"Public pages contain unresolved placeholders: {unresolved}")

    print("site checks passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"site checks failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
