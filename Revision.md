# LeetCode Revision Sheet

---

## 📦 Arrays

---

### 1. Two Sum

**🔗 Link:** https://leetcode.com/problems/two-sum/  
**💡 Difficulty:** Easy  
**🧩 Pattern:** Hash Map / Complement Lookup  

---

#### 🐢 Brute Force — O(n²) time | O(1) space

```python
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            return [i, j]
```

#### ⚡ Optimal — O(n) time | O(n) space

```python
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

#### 🧠 Insights / Tips

- Instead of searching for a pair, store what you *need* and check if you've seen it  
- One pass is enough — no need to pre-populate the map  
- Map stores `value → index`, not the other way around  

---