# jenkins

## Install at RedHat / CentOS-6

```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install -y jenkins

sudo service jenkins start
sudo service jenkins stop
sudo service jenkins restart
sudo chkconfig jenkins on


## 服务启动以后稍等一下
cat /var/lib/jenkins/secrets/initialAdminPassword
```

## First Run 配置

- Install suggested plugins
- Create First Admin User
  - jroot/jroot123
- Instance Configuration

## Usual Configuration

- Force UI in English
  - Click Manage Jenkins > Manage Plugins > ['Available' tab]
  - In the Filter, search for: Locale .
  - Click on Locale Plugin checkbox and Install without restart button.
  - After installation is complete:
    - Under Manage Jenkins > Configure System there should be a "Locale" section.
    - Enter the default language_LOCALE code for English: en_US
    - Click on Ignore browser preference and force this language to all users checkbox.

- Run command as root
  - <https://stackoverflow.com/questions/17096784/is-it-possible-to-allow-jenkins-to-access-the-files-that-only-root-or-some-speci?rq=1>
  - <https://stackoverflow.com/questions/29926773/run-shell-command-in-jenkins-as-root-user/31799780>
