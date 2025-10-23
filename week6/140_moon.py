from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # initialization
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True

        sentences = []
        return self.DFS_DP(s, 0, wordDict, dp, [], sentences)

    def DFS_DP(self, s: str, start: int,  wordDict: List[str], dp: List[bool], sentence: List[str], sentences: List[str]):
        if dp[-1] is True:
            # 마지막 단어까지 조건을 만족하면 sentence로 변환해서 sentences 리스트에 추가
            # 리턴값은 모든 가능한 문장의 리스트
            sentences.append(" ".join(sentence))
            return sentences
        
        for i in range(1, len(s)+1):
            for word in wordDict:
                w_len = len(word)
                if i - w_len >= 0 and dp[start + i] is False:
                    # i번째 char가 dp 조건을 만족하면 True로 설정
                    dp[start + i] = dp[start+i - w_len] and s[i-w_len:i] == word
                
                    if dp[start + i] is True:
                        # DFS 영역

                        # 만약 word가 dp 조건을 만족하면 sentence에 추가해서 후보군 생성
                        sentence.append(word)
                        # i번 전까지는 확인했으므로 string의 i번부터 새로 확인해주어야 함. 재귀적으로 DFS 호출
                        sentences = self.DFS_DP(s[i:], start+i, wordDict, dp, sentence, sentences)

                        # DFS + DP, DFS 순회하고 다시 위로 올라왔을 때 기존에 T로 설정해준 dp를 제거 및 문장 후보군에서 단어 제거
                        dp[start + i] = False
                        sentence.pop()

        return sentences
