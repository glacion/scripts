"""Used for retrieving the name and the url of all the repos that a user owns on GitHub.

Copyright (C) 2020 Ahmetcan Güvendiren

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

from typing import Dict, TypeVar, List


def get_json(username: str) -> List[Dict[str, any]]:
    """Returns the List of repos parsed from JSON retrieved from GitHub API"""
    import json
    import urllib.request
    url = f'https://api.github.com/users/{username}/repos'
    with urllib.request.urlopen(url) as response:
        return json.load(response)


def get_max_length(data: List[Dict[str, str]]) -> int:
    """Returns the length of the name of the repo with the longest name

    Used for determining the justification amount.
    """
    longest_repo: Dict[str, str] = max(
        data, key=lambda repo: len(repo['name']))
    return len(longest_repo['name'])


def output_data(data: List[Dict[str, str]]) -> None:
    """Outputs given data to console."""
    if not data:
        print(f'{args.username} has no repos.')
    else:
        max_len = get_max_length(data)
        print(f'{"Name":<{max_len}}    URL')
        for repo in data:
            print(f'{repo["name"]:<{max_len}}    {repo["html_url"]}')


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'username', help='Username of the user that you wish to see repos of')
    args = parser.parse_args()
    # res = get_json(args.username)
    # output_data(res)
    print(__doc__)