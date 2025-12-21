# My progress into data structure and algorithms

<center>

| DAY    | STATUS | PROBLEM | DESCRIPTION
| :--------:| :-------: | :-------: | :------- |
|  12/12/2025 |  😀  | Find Closest Number to Zero | Solved, but i need to look for some ideas because i could't think how to verify whether the abs(number) was in the list, and when it was true, how to return the greater number  |
|  13/12/2025 |  😀  | Merge Strings Alternately | Solved using string concatenations, after a saw that could be solved using list, reducing the time complexity at O(N), where  N is the length of word1 plus length word2, respectively |
|  14/12/2025 |  😀  | Roman to Integer | I was able to resolve this question without help, but afterwards see other solutions i noticed that i could've solved without a extra IF statement outside the while loop   |
|  14/12/2025 |  😀  | Is Subsequence | Solved without external help, but, i wrote len(s) == 0 and len(t) >= 0; the second condition is unnecessary, because the string length(t) will be zero or greater than zero. Another tweak was len(s) > len(t) rather than len(s) > 0 and len(t) == 0 which i had been written, because the old way wouldn't catch: len(s) = 4; len(t) = 3, for example, causing unnecessary loop  |
|  15/12/2025 |  🤔  | Best Time to Buy and Sell Stock | I could think about a solution but the algorithm is still confusing |
|  16/12/2025 |  😀  | Best Time to Buy and Sell Stock | Solved without help, but when i submitted the code i noticed the runtime a little slow, so, after search for ideas, i noticed that i was using function pre-built(max and min) and these calls to functions/methods has a high time cost.The solution was using ternary operation to replace methods call,resulting a faster code|
|  16/12/2025 |  😀  | Longest Common Prefix | Solved without help, but the space complexity could've been O(1).Rather than using an array to append the common characters between the strings, i could have simply returned  `s[:i]`. In the case when common substring is smaller than every string in the list. And returned `strs[0][:i]` when the substring has the same length as every string in the list(in this case, all the strings have the same length)|
|  17/12/2025 |  😀  | Summary Ranges | Solved without help, but after analyze other solutions i noticed that my question in the code was: "Where the range ends", and in the solutions the question was: "What is the range?". My question in the code implies that at the end of the loop i couldn't get the last range, because it doesn't finish yet and I need to check outside loop the last range, implies a double check because the question was: "where ends" and not "what is"|
|  18/12/2025 |  😀  | Product of Array Except Self | Solved with help, I had difficult to visualize the logic of left element X right element.The trick was using a variable start at 1, so the multiplication occurred with the elements, except the actual, making this for left and right, at the end, multiplying the left by the right |
|  19/12/2025 |  😀  |Merge Intervals |Solved without help, and in this case my solution isn't that bad at all, in general, it's good and my logic was similar to other solutions that had a good time and space complexity|
|  19/12/2025 |  😀  |Rotate Image |Solved without help,and in this case I had the idea to transpose the matrix and swap the elements from left to right, which works, and had a good time and space complexity|
<center>


## Emojis to use

| EMOJI    | DESCRIPTION 
| :--------:| :-------: 
| 😀       |   SOLVED  |
| 🤔       |   IN_PROGRESS  |
| ☹️       |   COULDN'T_SOLVE  |