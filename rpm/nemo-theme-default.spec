Name:       nemo-theme-default
# >> macros
%define theme_name base
# << macros

Summary:    Nemo Mobile default theme
Version:    1.0.5
Release:    3
Group:      System/GUI/Other
License:    BSD/LGPLv2.1
BuildArch:  noarch
URL:        https://github.com/nemomobile/nemo-theme-default
Source0:    %{name}-%{version}.tar.bz2
Requires:   gconf
BuildRequires: fdupes
BuildRequires: qt5-qmake
Provides:   qt-components-base-icons
Provides:   nemo-theme-graphics
Provides:   meegotouch-theme-graphics = 1.0.3
Obsoletes:  meegotouch-theme-graphics <= 1.0.2.1
Obsoletes:  meegotouch-theme-ce <= 0.1.26
Provides:  meegotouch-theme-ce = 0.1.26.1
 
%description
This package contains default theme graphic files.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install

%fdupes  %{buildroot}%{_datadir}

%post
Theme_Key="/meegotouch/theme/name"
Config_Src=`/usr/bin/gconftool-2 --get-default-source`

Theme_Name=`/usr/bin/gconftool-2 --direct --config-source $Config_Src \
            -g $Theme_Key`

if [ -z $Theme_Name ]; then
    echo "Setting theme name to %{theme_name}"
    /usr/bin/gconftool-2 --direct --config-source $Config_Src \
    -s -t string $Theme_Key %{theme_name}
fi

%files
%defattr(-,root,root,-)
%{_datadir}/themes/base/index.theme
%{_datadir}/themes/base/meegotouch/icons


