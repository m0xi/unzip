# unzip

This script is meant to be very simple. It will take all the zip files in whatever directory you run it, unzip them, and delete the original zip file.

If there are leftover zips, there are two possible reasons:
1. The file has the extension .zip - but is not actually a .zip file. (that's why we use the magic module)
2. The .zip file is a .zip but it is a duplicate so it was ignored. 
