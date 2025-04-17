%global octpkg hdf5oct

Summary:	MATLAB compatible high-level functions for HDF5 file I/O
Name:		octave-hdf5oct
Version:	1.0.0
Release:	1
License:	LGPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/hdf5oct/
Url:		https://github.com/gapost/hdf5oct
Source0:	https://github.com/gapost/hdf5oct/archive/refs/tags/%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 6.0.0
BuildRequires:	hdf5-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
MATLAB compatible high-level functions for HDF5 file I/O.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

