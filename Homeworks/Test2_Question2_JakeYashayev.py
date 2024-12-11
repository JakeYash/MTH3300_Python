#Question #2 not using .index()
def cipher(letlist,k):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #outerloop goes through given list of letters
    for i in range(len(letlist)):
        #inner loop goes through alphabet to find match
        for j in range(len(abc)):
            if (letlist[i] == abc[j]):
                #once a match is found, the letter in the provided list is 
                #advanced by the number of places = to the key
                try:
                    letlist[i] = abc[j+k]
                    break
                except:
                    #if that is beyond the range of the alphabet, you need to 
                    #go around, the mod26 ensures it works for very large k 
                    #values
                    x = (j+k - 26)%26
                    letlist[i] = abc[x]
                    break