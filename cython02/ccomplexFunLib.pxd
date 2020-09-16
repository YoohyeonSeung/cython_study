cdef extern from "complexFunLib.h":
    void mp_mlt_exp_c4(float complex* k, float complex* ee, int sz, float complex* res, int threads);
    void mp_mlt_exp_c8(double complex* k, double complex* ee, int sz, double complex* res, int threads);