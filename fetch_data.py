import requests

url = "https://leetcode.com/graphql"

query = """
query {
  matchedUser(username: "your_username") {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

response = requests.post(url, json={"query": query})
print(response.json())