from collections import namedtuple
import os
import sys

from github import Github

Repo = namedtuple('Repo', 'name stars forks')


GH_USER = os.environ.get('GH_USER')
GH_PW = os.environ.get('GH_PW')
if not GH_USER or not GH_PW:
    print('Please set GH_USER and GH_PW env vars')
    sys.exit(1)


def get_user(user):
    gh = Github(GH_USER, GH_PW)
    return gh.get_user(user)


def get_repo_stats(user):
    for repo in user.get_repos():
        if repo.fork:
            continue

        yield Repo(name=repo.name,
                   stars=repo.stargazers_count,
                   forks=repo.forks_count)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        user = 'pybites'
    else:
        user = sys.argv[1]

    try:
        user = get_user(user)
    except Exception as exc:
        print('Cannot get user {}: '.format(user))
        print(exc)
        sys.exit(1)

    print('{} ({}) - followers: {} / following: {}'.format(user.login,
                                                           user.name,
                                                           user.followers,
                                                           user.following))
    print()

    repo_stats = get_repo_stats(user)

    fmt = '{:<44} | {:<5} | {:<5}'
    print(fmt.format('Repo name', 'Stars', 'Forks'))
    print('-' * 60)

    for repo in sorted(repo_stats,
                       key=lambda r: (r.stars + r.forks)/2,
                       reverse=True):
        print(fmt.format(repo.name, repo.stars, repo.forks))
