# recverse-proxy 
- 성능 
- 부하분산(LB) 
- 가상호스트 및 라우팅 


## python server
```bash
$ python -m http.server --directory pyweb1 8001
$ python -m http.server --directory pyweb1 8002
$ python -m http.server --directory 8003

# 아래 방식으로 동작하는 함수를 만들어 보세요 (hint: *args  **kargs)
run_server() 로도 호출 가능
run_server(8000)
run_server(8000, directory="abc")로도 호출 가능
run_server(directory="abc", port=8000)로도 호출가능 


## nGrinder
- http://localhost:8080(ID: admin / PW:admin)
```bash
$ pwd
~/app
$ tree -L 2
.
├── ngrinder-agent
│   ├── lib
│   ├── run_agent.bat
│   ├── run_agent.sh
│   ├── run_agent_bg.sh
│   ├── run_agent_internal.bat
│   ├── run_agent_internal.sh
│   ├── stop_agent.bat
│   └── stop_agent.sh
└── ngrinder-controller
    └── ngrinder-controller-3.5.9-p1.war
```

# controller
```bash
$ sudo apt install openjdk-11-jdk
$ wget https://github.com/naver/ngrinder/releases/download/ngrinder-3.5.9-p1-20240613/ngrinder-controller-3.5.9-p1.war                                                                                           $ mkdir ngrinder-controller                                                                                                                                                                                      $ mv ngrinder-controller-3.5.9-p1.war ngrinder-controller  
$ java -jar ngrinder-controller-3.5.9-p1.war
```


## nginx
- https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview
```bash
$ sudo service nginx restart
$ sudo service nginx stop
$ sudo service nginx start
$ sudo service nginx status #-> worker 16ea
$ sudo nginx -t # syntax check
```

# agent
```bash
$ run_agent.sh
```

## .zshrc 수정  
```bash
# JAVA_HOME
# nGrinder
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```
