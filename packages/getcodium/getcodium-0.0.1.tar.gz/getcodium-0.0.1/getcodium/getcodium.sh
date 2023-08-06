#!/bin/bash

_args_=($@) # all parameters from terminal.
printf "args\n\t${_args_[*]}\n"

# tools check
_t_satisfied_=true
_t_is_n_i_="is not installed"
for t in curl sha256sum
do
    if ! [[ -x $(which $t) ]]; then
        _t_satisfied_=false
        echo "> $t"
    fi
done
if ! $_t_satisfied_; then
    echo "The above is/are not installed, getcodium exit."
    return
fi

# print help
if [[ ${_args_} == *\ -h ]] ; then
    echo ""
    return
fi

# get pkg_ext
_release_id_=$(cat /etc/os-release | grep -Eo  '^ID=(\S*)')
_release_id_=${_release_id_:3}
_pkg_ext_=$([[ 'ubuntu debian' == *${_release_id_}* ]] && echo "deb" || \
    echo "deb")
printf "pkg_ext\n\t${_pkg_ext_}\n"

# is debian?
[[ $_pkg_ext_ == 'deb' ]] && _is_debian_=true || _is_debian_=false
printf "is_debian\n\t"; $is_debian && printf 'Y' || printf 'N'; printf "\n"

# get_kernel
_kernel_=$(echo `uname -s` | tr '[:upper:]' '[:lower:]')
printf "kernel\n\t${_kernel_}\n"

# get processor
_processor_=$(echo `uname -p` | tr '[:upper:]' '[:lower:]')
_processor_=$([[ 'x86_64 amd64'==*${_processor_}* ]] && echo "amd64" || \
    echo "amd64")
printf "processor\n\t${_processor_}\n"

# specified mirror
_mirror_=$([[ -n "${_args_}" ]] && echo ${_args_} || echo 'BFSU')
printf "mirror\n\t${_mirror_}\n"

# get mirror url
_mirror_url_=$(cat ./codium.mirrors | grep ${_mirror_})
_mirror_url_=(${_mirror_url_})
_mirror_url_=${_mirror_url_[1]}
printf "mirror_url\n\t${_mirror_url_}\n"

# download pkg
_pkg_name_=$(curl $_mirror_url_ | grep $_processor_ | \
    grep -Eo ">\S*.$_pkg_ext_<")
_pkg_name_=${_pkg_name_:1:-1}
[[ $_pkg_name_ == */* ]] && return
echo "download ${_pkg_name_} . . ."
curl $_mirror_url_$_pkg_name_ -o $_pkg_name_

# download pkg sha256
_pkgsha256_name_=$(curl $_mirror_url_ | grep $_processor_ | \
    grep -Eo ">\S*.${_pkg_ext_}.sha256<")
_pkgsha256_name_=${_pkgsha256_name_:1:-1}
[[ $_pkgsha256_name_ == */* ]] && return
echo "download ${_pkg_name_}.sha256 . . ."
curl $_mirror_url_$_pkgsha256_name_ -o $_pkgsha256_name_

_sha256sum_check_=$(cat $_pkgsha256_name_ | sha256sum --check)

if [[ $_sha256sum_check_ == *OK ]]; then
    if $_is_debian_; then
        printf "\nsudo dpkg --install $_pkg_name_\n\n"
        sudo dpkg --install $_pkg_name_
        [[ $_pkg_name_ == */* ]] && echo "getcodium crashs, exit." && \
        return
        [[ $_pkgsha256_name_ == */* ]] && echo "getcodium crashs, exit." && \
        return
        rm -rf $_pkg_name_ $_pkgsha256_name_
    fi
    echo "codium is installed. HAPPY CODING :-) "
else
    echo "sha256sum checking failed! getcodium exit."
fi

# wait for you to contribute the code.