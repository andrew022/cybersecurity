#!/bin/bash

echo "Please input a directory path:"
ls
read path
echo "Please enter a permission number:"
read permission
chmod $permission $path
echo "You have granted chmod permission of $permission to $path."
ls -l $path