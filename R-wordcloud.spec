#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-wordcloud
Version  : 2.6
Release  : 4
URL      : https://cran.r-project.org/src/contrib/wordcloud_2.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/wordcloud_2.6.tar.gz
Summary  : Word Clouds
Group    : Development/Tools
License  : LGPL-2.1
Requires: R-wordcloud-lib = %{version}-%{release}
Requires: R-RColorBrewer
Requires: R-Rcpp
BuildRequires : R-RColorBrewer
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
# wordcloud
Functionality to create pretty word clouds, visualize differences and similarity between documents, and avoid over-plotting in scatter plots with text.

%package lib
Summary: lib components for the R-wordcloud package.
Group: Libraries

%description lib
lib components for the R-wordcloud package.


%prep
%setup -q -c -n wordcloud
cd %{_builddir}/wordcloud

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589565908

%install
export SOURCE_DATE_EPOCH=1589565908
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wordcloud
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wordcloud
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wordcloud
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc wordcloud || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/wordcloud/DESCRIPTION
/usr/lib64/R/library/wordcloud/INDEX
/usr/lib64/R/library/wordcloud/Meta/Rd.rds
/usr/lib64/R/library/wordcloud/Meta/data.rds
/usr/lib64/R/library/wordcloud/Meta/features.rds
/usr/lib64/R/library/wordcloud/Meta/hsearch.rds
/usr/lib64/R/library/wordcloud/Meta/links.rds
/usr/lib64/R/library/wordcloud/Meta/nsInfo.rds
/usr/lib64/R/library/wordcloud/Meta/package.rds
/usr/lib64/R/library/wordcloud/NAMESPACE
/usr/lib64/R/library/wordcloud/NEWS
/usr/lib64/R/library/wordcloud/R/wordcloud
/usr/lib64/R/library/wordcloud/R/wordcloud.rdb
/usr/lib64/R/library/wordcloud/R/wordcloud.rdx
/usr/lib64/R/library/wordcloud/data/SOTU.RData
/usr/lib64/R/library/wordcloud/help/AnIndex
/usr/lib64/R/library/wordcloud/help/aliases.rds
/usr/lib64/R/library/wordcloud/help/paths.rds
/usr/lib64/R/library/wordcloud/help/wordcloud.rdb
/usr/lib64/R/library/wordcloud/help/wordcloud.rdx
/usr/lib64/R/library/wordcloud/html/00Index.html
/usr/lib64/R/library/wordcloud/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/wordcloud/libs/wordcloud.so
