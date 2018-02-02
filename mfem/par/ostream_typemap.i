%module ostream_typemap

 // recipe for ostream
%typemap(in) std::ostream& (boost_ofdstream *stream=NULL) {
  FILE *f=PyFile_AsFile($input); // Verify the semantics of this
  if (!f) {
    SWIG_Error(SWIG_TypeError, "File object expected.");
    SWIG_fail;
  }
  else {
    // If threaded incrment the use count
    stream = new boost_ofdstream(fileno(f), io::never_close_handle);
    $1 = new std::ostream(stream);
  }
}
%typemap(typecheck, precedence=SWIG_TYPECHECK_STRING_ARRAY) std::ostream& {
  if (PyFile_Check($input)){
    $1 = 1;
  } else {
    $1 = 0;
  }
}
%typemap(freearg) std::ostream& {
  delete $1;
  delete stream$argnum;
}
