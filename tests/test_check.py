"""Unit tests for scripts/check.py, with no network: plugin.json is faked."""
import io, os, sys, unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
import check  # noqa: E402

README = "## X\n\n- **[a](u)**: a.\n- **[b](u)**: b.\n- **[c](u)**: c.\n\n## Command-line tools\n"


def fetch(repo):
    return {"name": repo.split("/")[1], "description": "desc"}


class CheckTest(unittest.TestCase):
    def test_entries_without_a_github_repo_are_skipped_with_a_warning(self):
        market = {"plugins": [
            {"name": "a", "source": {"source": "github", "repo": "o/a"}, "description": "desc"},
            {"name": "b", "source": "./plugins/b", "description": "desc"},
            {"name": "c", "source": {"source": "url", "url": "https://example.com/c.git"}, "description": "desc"},
        ]}
        out = io.StringIO()
        with redirect_stdout(out):
            errors = check.check(market, README, fetch)
        self.assertEqual(errors, [])
        self.assertIn("b: not a GitHub repo source", out.getvalue())
        self.assertIn("c: not a GitHub repo source", out.getvalue())

    def test_a_description_mismatch_is_reported(self):
        market = {"plugins": [
            {"name": "a", "source": {"source": "github", "repo": "o/a"}, "description": "other"},
            {"name": "b", "source": {"source": "github", "repo": "o/b"}, "description": "desc"},
            {"name": "c", "source": {"source": "github", "repo": "o/c"}, "description": "desc"},
        ]}
        errors = check.check(market, README, fetch)
        self.assertEqual(len(errors), 1)
        self.assertIn("a: description differs", errors[0])

    def test_readme_order_must_match(self):
        market = {"plugins": [
            {"name": n, "source": {"source": "github", "repo": f"o/{n}"}, "description": "desc"} for n in ["b", "a", "c"]
        ]}
        errors = check.check(market, README, fetch)
        self.assertTrue(any("README order/list differs" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
