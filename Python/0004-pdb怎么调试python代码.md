# pdb怎么调试python代码

1. `python -m pdb script.py`如果报错会停在报错的地方

2. 在代码中使用pdb，代码里设置断点，即使不报错也会停止

   ```python
   import pdb;
   pdb.set_trace();
   ```

3. ipdb包可以打开ipython

