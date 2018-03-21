echo "Install programming languages"
brew install cmake pkg-config python3 go node perl ruby rust swig bazel jq imagemagick

brew install tbb tcl-tk

echo "Install system tools"
brew install ssh-copy-id zsh tmux ranger tree unrar fontconfig curl wget axel aria2 the_silver_searcher watch htop nload

echo "Install vim with python3 support"
brew install vim --with-python3

echo "Install quick look plugins"
brew cask install qlcolorcode qlstephen qlmarkdown quicklook-json qlprettypatch quicklook-csv betterzipql qlimagesize webpquicklook suspicious-package quicklookase qlvideo
