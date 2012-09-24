%define		plugin	class
Summary:	jQuery plugin that helps you to create and work with classes/objects
Name:		jquery-%{plugin}
Version:	1.1.0
Release:	2
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/kilhage/class.js/tarball/v.%{version}/%{name}-%{version}.tgz
# Source0-md5:	ff897f42f94348066a6df8d6ac382b48
URL:		https://github.com/kilhage/class.js
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
This library allows you to create Class-like functions in an very
effective and nice way.

%prep
%setup -qc
mv *-%{plugin}.js-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}
