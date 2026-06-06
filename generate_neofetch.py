#!/usr/bin/env python3
import os, time, requests

USERNAME = "IamShariqMukadam"
H = {
    "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', '')}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def trunc(s, n=50): s=str(s); return s[:n]+"..." if len(s)>n else s

def get(url, headers=None):
    try: return requests.get(url, headers=headers or H, timeout=10).json()
    except: return {}

def get_loc(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/stats/contributors"
    for _ in range(3):
        try:
            r = requests.get(url, headers=H, timeout=15)
            if r.status_code == 200: return r.json()
            elif r.status_code == 202: time.sleep(3)
        except: pass
    return []

TEMPLATE = """<svg width="100%" viewBox="0 0 680 396" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Shariq Mukadam — GitHub Profile</title>
  <desc>Neofetch-style profile card with live GitHub stats</desc>
  <rect width="680" height="396" rx="10" fill="#0D1117"/>
  <rect x="0.5" y="0.5" width="679" height="395" rx="9.5" fill="none" stroke="#30363D" stroke-width="1"/>
  <circle cx="22" cy="22" r="6" fill="#FF5F57"/>
  <circle cx="42" cy="22" r="6" fill="#FFBD2E"/>
  <circle cx="62" cy="22" r="6" fill="#28CA41"/>
  <text x="80" y="27" font-family="'Courier New',Courier,monospace" font-size="12" fill="#6E7681">shariq@github \u2014 zsh</text>
  <line x1="0" y1="40" x2="680" y2="40" stroke="#21262D" stroke-width="1"/>
  <text font-family="'Courier New',Courier,monospace" font-size="14" font-weight="bold"><tspan x="24" y="65" fill="#26C6DA">shariq</tspan><tspan fill="#D4D4D4">@</tspan><tspan fill="#26C6DA">github</tspan></text>
  <line x1="24" y1="73" x2="480" y2="73" stroke="#26C6DA" stroke-width="0.5"/>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="96" fill="#26C6DA">title</tspan><tspan fill="#3D3D3D"> ........ </tspan><tspan fill="#D4D4D4">AI/ML Engineer | Data Analyst</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="118" fill="#26C6DA">location</tspan><tspan fill="#3D3D3D"> ..... </tspan><tspan fill="#D4D4D4">Pune, India</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="140" fill="#26C6DA">education</tspan><tspan fill="#3D3D3D"> .... </tspan><tspan fill="#D4D4D4">BCA @ BVDU Pune \u2014 CGPA: 8.61 / 10</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="162" fill="#26C6DA">status</tspan><tspan fill="#3D3D3D"> ....... </tspan><tspan fill="#28CA41">&#x25CF; Open to Work</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="184" fill="#26C6DA">currently</tspan><tspan fill="#3D3D3D"> .... </tspan><tspan fill="#D4D4D4">Deploying AI agents &amp; analytics that solve real problems</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="206" fill="#26C6DA">wip[0]</tspan><tspan fill="#3D3D3D"> ....... </tspan><tspan fill="#D4D4D4">__WIP0__</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="228" fill="#26C6DA">wip[1]</tspan><tspan fill="#3D3D3D"> ....... </tspan><tspan fill="#D4D4D4">__WIP1__</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="250" fill="#26C6DA">wip[2]</tspan><tspan fill="#3D3D3D"> ....... </tspan><tspan fill="#D4D4D4">__WIP2__</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="272" fill="#26C6DA">fun_fact</tspan><tspan fill="#3D3D3D"> ..... </tspan><tspan fill="#D4D4D4">Built AI agents that negotiate contracts + scrape 400+ jobs</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="300" fill="#6E7681">- </tspan><tspan fill="#D4D4D4">GitHub Stats </tspan><tspan fill="#6E7681">------------------------------------------------.--</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="322" fill="#6E7681">  . </tspan><tspan fill="#26C6DA">Repos</tspan><tspan fill="#3D3D3D">: .... </tspan><tspan fill="#D4D4D4">__REPOS__ </tspan><tspan fill="#CE9178">{Contributed: __CONTRIBUTED__}</tspan><tspan x="380" fill="#6E7681"> | </tspan><tspan fill="#26C6DA">Stars</tspan><tspan fill="#3D3D3D">: ... </tspan><tspan fill="#D4D4D4">__STARS__</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="344" fill="#6E7681">  . </tspan><tspan fill="#26C6DA">Commits</tspan><tspan fill="#3D3D3D">: .... </tspan><tspan fill="#D4D4D4">__COMMITS__</tspan><tspan x="380" fill="#6E7681"> | </tspan><tspan fill="#26C6DA">Followers</tspan><tspan fill="#3D3D3D">: ... </tspan><tspan fill="#D4D4D4">__FOLLOWERS__</tspan></text>
  <text font-family="'Courier New',Courier,monospace" font-size="13"><tspan x="24" y="366" fill="#CE9178">&apos;i</tspan><tspan fill="#6E7681"> . </tspan><tspan fill="#26C6DA">Lines of Code</tspan><tspan fill="#3D3D3D">: </tspan><tspan fill="#D4D4D4">__LOC__ ( </tspan><tspan fill="#4EC9B0">__ADDITIONS__++</tspan><tspan fill="#D4D4D4">,  </tspan><tspan fill="#F44747">__DELETIONS__--</tspan><tspan fill="#D4D4D4"> )</tspan></text>
</svg>"""

def fetch():
    user = get(f"https://api.github.com/users/{USERNAME}")
    repos = get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=pushed")
    if not isinstance(repos, list): repos = []
    repos = [r for r in repos if isinstance(r, dict)]

    stars = sum(r.get("stargazers_count", 0) for r in repos)
    wip = [r["name"] for r in repos[:3] if r.get("name")]

    sc = get(
        f"https://api.github.com/search/commits?q=author:{USERNAME}&per_page=1",
        {**H, "Accept": "application/vnd.github.cloak-preview+json"}
    )
    commits = sc.get("total_count", 0)

    q = '''{ user(login: "%s") { repositoriesContributedTo(first:1, includeUserRepositories:true, contributionTypes:[COMMIT,ISSUE,PULL_REQUEST,REPOSITORY]) { totalCount } } }''' % USERNAME
    try:
        gr = requests.post("https://api.github.com/graphql", json={"query": q}, headers=H, timeout=10).json()
        contributed = gr["data"]["user"]["repositoriesContributedTo"]["totalCount"]
    except: contributed = 0

    additions = deletions = 0
    for repo in repos:
        if repo.get("fork"): continue
        stats = get_loc(repo["name"])
        if isinstance(stats, list):
            for c in stats:
                if isinstance(c, dict) and c.get("author", {}).get("login", "").lower() == USERNAME.lower():
                    for w in c.get("weeks", []):
                        additions += w.get("a", 0)
                        deletions += w.get("d", 0)

    loc = additions - deletions

    return {
        "repos": user.get("public_repos", "?"),
        "followers": user.get("followers", "?"),
        "stars": f"{stars:,}",
        "commits": f"{commits:,}",
        "contributed": contributed,
        "wip": (wip + ["—","—","—"])[:3],
        "loc": f"{loc:,}",
        "additions": f"{additions:,}",
        "deletions": f"{deletions:,}"
    }

def generate(s):
    svg = TEMPLATE
    svg = svg.replace("__WIP0__", esc(trunc(s["wip"][0])))
    svg = svg.replace("__WIP1__", esc(trunc(s["wip"][1])))
    svg = svg.replace("__WIP2__", esc(trunc(s["wip"][2])))
    svg = svg.replace("__REPOS__", str(s["repos"]))
    svg = svg.replace("__CONTRIBUTED__", str(s["contributed"]))
    svg = svg.replace("__STARS__", s["stars"])
    svg = svg.replace("__COMMITS__", s["commits"])
    svg = svg.replace("__FOLLOWERS__", str(s["followers"]))
    svg = svg.replace("__LOC__", s["loc"])
    svg = svg.replace("__ADDITIONS__", s["additions"])
    svg = svg.replace("__DELETIONS__", s["deletions"])
    return svg

if __name__ == "__main__":
    stats = fetch()
    with open("neofetch.svg", "w", encoding="utf-8") as f:
        f.write(generate(stats))
    print(f"Done: {stats}")
