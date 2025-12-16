# My progress into data structure and algorithms

<center>

| DAY    | STATUS | PROBLEM | DESCRIPTION
| :--------:| :-------: | :-------: | :------- |
|  12/12/2025 |  😀  | 2239 | Solved, but i need to look for some ideas because i could't think how to verify whether the abs(number) was in the list, and when it was true, how to return the greater number  |
|  13/12/2025 |  😀  | 1768 | Solved using string concatenations, after a saw that could be solved using list, reducing the time complexity at O(N), where  N is the length of word1 plus length word2, respectively |
|  14/12/2025 |  😀  | 13 | I was able to resolve this question without help, but afterwards see other solutions i noticed that i could've solved without a extra IF statement outside the while loop   |
|  14/12/2025 |  😀  | 392 | Solved without external help, but, i wrote len(s) == 0 and len(t) >= 0; the second condition is unnecessary, because the string length(t) will be zero or greater than zero. Another tweak was len(s) > len(t) rather than len(s) > 0 and len(t) == 0 which i had been written, because the old way wouldn't catch: len(s) = 4; len(t) = 3, for example, causing unnecessary loop  |
|  15/12/2025 |  🤔  | 121 | I could think about a solution but the algorithm is still confusing |
|  16/12/2025 |  😀  | 121 | Solved without help, but when i submitted the code i noticed the runtime a little slow, so, after search for ideas, i noticed that i was using function pre-built(max and min) and these calls to functions/methods has a high time cost.The solution was using ternary operation to replace methods call,resulting a faster code|
|  16/12/2025 |  😀  | 14 | Solved without help, but the space complexity could've been O(1).Rather than using an array to append the common characters between the strings, i could have simply returned  `s[:i]`. In the case when common substring is smaller than every string in the list. And returned `strs[0][:i]` when the substring has the same length as every string in the list(in this case, all the strings have the same length)|

<center>


## Emojis to use

| EMOJI    | DESCRIPTION 
| :--------:| :-------: 
| 😀       |   SOLVED  |
| 🤔       |   IN_PROGRESS  |
| ☹️       |   COULDN'T_SOLVE  |