/*!
 * \addtogroup MCU_COMMON
 * \{
 *
 * \file        mcu_common.c
 *
 * \brief       MCU Common implementation used for test.
 *
 * Copyright (c) 2016 Autoliv Electronics AB
 *
 * All rights reserved. Property of Autoliv Electronics AB.
 * Restricted rights to use, duplicate or disclose this code
 * are granted through contract.
 * \}
 */

/* **** Includes **** */

#include "support/mcu_common/mcu_common.h"

/*! \qacexception 553: Translation unit contains no external linkage. Intentional. */
/* PRQA S 553 EOF */

/* **** Global Variables **** */

#ifdef __GNUC__

U32 MCUC_addedOnlyForTest;

#endif
