> 얄팍한 코딩사전 <제대로 파는 Git&GitHub> 강의 내용 정리

## Git을 배워야 하는 이유
* Git은 분산형 버전 관리 시스템(VCS)이다.
    * 프로젝트의 버전을 과거로 되돌리거나 특정 내역을 취소할 수 있다.
    * 프로젝트의 여러 모드를 쉽게 전환하고 관리할 수 있다.
    * 여러 사람들이 협업할 수 있다.

## Git 최초 설정
* Git 전역으로 사용자 이름 및 이메일 주소 설정(GitHub 계정과 별개)
    * Git Bash에서 다음 명령어로 설정
        git config --global user.name "(이름)"
        git config --global user.email "(이메일)"

* 기본 브랜치명 변경
    git config --global init.defaultBranch main

