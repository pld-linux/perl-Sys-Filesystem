#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Sys
%define		pnam	Filesystem
Summary:	Sys::Filesystem - Retrieve list of filesystems and their properties
Name:		perl-Sys-Filesystem
Version:	1.408
Release:	1
License:	apache
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0fee73467785f3d8372b9a2f0356cbcd
# generic URL, check or change before uncommenting
#URL:		https://metacpan.org/release/Sys-Filesystem
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Module-Pluggable >= 4.8
BuildRequires:	perl-Params-Util >= 1.00
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Filesystem is intended to be a portable interface to list and
query filesystem names and their properties. At the time of writing
there were only Solaris and Win32 modules available on CPAN to perform
this kind of operation. This module hopes to provide a consistent API
to list all, mounted, unmounted and special filesystems on a system,
and query as many properties as possible with common aliases wherever
possible.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes CREDITS INSTALL README TODO
%{perl_vendorlib}/Sys/Filesystem.pm
%{perl_vendorlib}/Sys/Filesystem
%{_mandir}/man3/Sys::Filesystem*.3*
