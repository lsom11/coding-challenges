high <- function(x){
  words <- strsplit(x," ")[[1]]
  word_scores <- c()
  for (i in seq_along(words)) {
    w <- tolower(words[i])
    word_scores[i] <- sum(as.numeric(factor(strsplit(w,"")[[1]],levels=letters)))
  }
  words[which.max(word_scores)]
}