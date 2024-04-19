{ pkgs, config, ... }:

{
  packages = [
    pkgs.git
    pkgs.zlib
    pkgs.gcc
    pkgs.cargo
    pkgs.gnuplot
  ];
  languages.python = {
    enable = true;
    poetry.enable = true;
  };
}
