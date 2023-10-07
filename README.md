
# GPT-2-straightforward

### Why Window Length for Prompt ? (experimental)

As text is generated, the length gets longer and longer and the computational resources also increase. If it's running on a limited device, it can potentially be a problem. the attention mechanism needs to consider more tokens, which intensifies the computational load.

    # Prompt for text generation
    sequence = input("start with: ")
    
    # by spaces between words. 
    window_length = 0 # Set it to 0 in order to consider all the text.

