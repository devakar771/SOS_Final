Implemeted the Encoder-Decoder mechanism of Image Captioning using Attention Mechnism. The model was trained on the Flickr 8k dataset.

# The encoder model uses InceptionV3 as base model to extract features from the images.
# The attention part links up the extracted features with the captions of the image.
# Decoder is implemented using GRU.
# Model trained weights can be found here.
  https://drive.google.com/file/d/11mk5t6pCyaSjAExNr7j9W9_83hLUfK6Y/view?usp=sharing

The model obtained an average BLEU score of 0.51 on the validation data of 7000 captions.