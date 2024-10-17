%define rbname imlib2
%define version 0.5.2
%define release %mkrel 7

Summary: Imlib2 bindings for Ruby
Name: ruby-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: BSD-like
URL: https://ruby-imlib2.rubyforge.org/
Source0: %{rbname}-ruby-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel 
BuildRequires: imlib2-devel

%description
Imlib2 bindings for Ruby.

%prep
%setup -q -n %{rbname}-ruby-%{version}

%build
ruby extconf.rb
make

%install
make install DESTDIR=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO doc examples
%{ruby_sitearchdir}/%{rbname}.so


