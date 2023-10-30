#!/usr/bin/env python3
"""
Test cases for GithubOrgClient
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
from fixtures import org_payload, repos_payload, expected_repos, apache2_reposi


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(test_class.ORG_URL.format(org=org_name))

    def test_has_license(self, repo, license_key, expected_result):
        '''Test GithubOrgClient.has_license'''
        github_org_client = GithubOrgClient('test_organization')
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos')
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration Test for GithubOrgClient'''

    @classmethod
    def setUpClass(cls, org_payload, repos_payload, expected_repos, apache2_repos):
        '''Setup for the test class'''
        cls.org_payload = org_payload
        cls.repos_payload = repos_payload
        cls.expected_repos = expected_repos
        cls.apache2_repos = apache2_repos
        cls.get_patcher = patch('client.requests.get')

        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            cls.org_payload,
            cls.repos_payload,
            cls.expected_repos,
            cls.apache2_repos
        ]

    @classmethod
    def tearDownClass(cls):
        '''Teardown for the test class'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Test GithubOrgClient.public_repos method'''
        github_org_client = GithubOrgClient('test_organization')
        repos = github_org_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        '''Test GithubOrgClient.public_repos method with license argument'''
        github_org_client = GithubOrgClient('test_organization')
        repos = github_org_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
