## Python2系とPython3系について
Pythonにはバージョンが存在していて（もちろんjavaにもある)、  
2と3は互換性がありません。　　

例えば

``` python
print "2系ならこれで表示できる"

print("3系はこれじゃないと表示できない")

```
基本的な文法でも大分差があります。
pythonプログラムを実行する前に  
``` python -V ``` 

でバージョンを確認できます。  
これで２系が表示されていたら  
``` python3 -V ```  

で確認してみましょう。  
それで３系が表示されるのなら、Pythonプログラムを実行する際は  

``` python3 fail_name.py ```  
で行えば3系が使用されます。   

特に理由がなければ3系を使うのがいいかと。
細かい点は[Python2からPython3.0での変更点](https://qiita.com/CS_Toku/items/353fd4b0fd9ed17dc152)を参考に。
