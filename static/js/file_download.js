
      document.addEventListener("DOMContentLoaded",function(){
      this.querySelector(".icon").addEventListener("click",function(){
        let waitClass = "waiting",
          runClass = "running",
          cl = this.classList;

        if (!cl.contains(waitClass) && !cl.contains(runClass)) {
          cl.add(waitClass);
          setTimeout(function(){
            cl.remove(waitClass);
            setTimeout(function(){
              cl.add(runClass);
              setTimeout(function(){
                cl.remove(runClass);
              }, 4000);
            }, 200);
          }, 1800);
        }
      });
    });



    function text_out(){

      var fileInput = document.getElementById('file-field');


      var p = document.getElementById('name_file1');
      var form = new FormData();
      form.append("file", fileInput.files[0]);

      var xhr = new XMLHttpRequest();

      xhr.open('POST', "/download_file", false);

      xhr.send(form);

      xhr.onload = function() {console.log("Отправка завершена ", fileInput);  };
      p.innerHTML = 'Эмбеддинг файла ' + fileInput.value + ' = 123456789 , status = ' + xhr.statusText;
    }
