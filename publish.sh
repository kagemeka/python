python3 setup.py \
  sdist \
  bdist_wheel

twine upload dist/*

sudo rm -r dist/*