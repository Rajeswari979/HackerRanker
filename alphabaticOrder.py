def designerPdfViewer(h, word):
    # Write your code here
    a = []
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(word)):
        if word[i] in alpha:
            index_of_word = alpha.index(word[i])
            a.append(h[index_of_word])
    return len(a) * max(a)
            
        
