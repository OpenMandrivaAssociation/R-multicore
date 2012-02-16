%global packname  multicore
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.1_6
Release:          1
Summary:          Parallel processing of R code on machines with multiple cores or CPUs
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/multicore/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/multicore/multicore_0.1-6.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
This package provides a way of running parallel computations in R on
machines with multiple cores or CPUs. Jobs can share the entire initial
workspace and it provides methods for results collection.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
