/*!
 * \addtogroup MCU
 * \{
 *
 * \file    aurix/mcu_family.c
 *
 * \brief   MCU Aurix family implementation.
 *
 * Copyright (c) 2015 Autoliv Electronics AB
 *
 * All rights reserved. Property of Autoliv Electronics AB.
 * Restricted rights to use, duplicate or disclose this code
 * are granted through contract.
 * \}
 */

/* **** Includes **** */

#include "types.h"

/*! \qacexception 0303: Cast between a pointer to volatile object and an integral type. Register access */
/*! \qacexception 3345: Statement contains more than one access to objects that are volatile. Register access */
/*! \qacexception 3120: Hard-coded 'magic' integer constant. Register values. */
/* PRQA S 0303, 3120, 3345 EOF */

/* **** Defines **** */


/* **** Typedefs **** */

/* **** Static Function Declarations **** */

static void setK2Divider(U8 divider);
static void wait(U16 delayUs, U8 divider);
/*!
 * Encapsulation of the embedded assembler snippet that implements the spinlock core atomic
 * instruction.
 *
 * \param[in] resource  A pointer to the spinlock resource variable.
 *
 * \return Zero is returned if the lock is locked at time the function is called.
 *         1 if lock is already locked prior this function call.
 */
static U32 tryToGetLock(U32 *resource);
static void spinlockLock(U32 *resource, U32 timeout);
static void spinlockUnlock(U32 *resource);

/* **** Static Variables **** */

static U32 safetyEndinitSpinlock = 0u;

/* **** Global Variables **** */

/* **** Static Function Definitions **** */

static void setK2Divider(U8 divider)
{

}

static void wait(U16 delayUs, U8 divider)
{

}

/*! \qacexception 3206: Parameter resource is used in inline assembler, QAC does not detect this. */
/* PRQA S 3206 ++ */
static U32 tryToGetLock(U32 *resource)
{

}

/* PRQA S 3206 -- */

static void spinlockLock(U32 *resource, U32 timeout)
{


}

static void spinlockUnlock(U32 *resource)
{

}

/* **** Function Definitions **** */

#if defined(APPLICATION) & !defined(UNIT_TESTS) /* To be able to build the bootloader */
void MCU_getCsaAndPsw(U8 level, CsaArray **csa, U8 *ioMode, U8 *prs, U32 depth) /* PRQA S 3651 */
{

}

void MCU_enterUserMode(void)
{

}

void MCU_enterSupervisorMode(void)
{

}
#else
void MCU_enterSupervisorMode(void){}
void MCU_enterUserMode(void){}
#endif

void MCU_unlockRegisters(void)
{

}

void MCU_lockRegisters(void)
{

}

void MCU_unlockSafetyRegisters(void)
{

}

void MCU_lockSafetyRegisters(void)
{

}

void MCU_init(void)
{

}

void MCU_reset(void)
{

}

void MCU_initClocks(void)
{

} /* PRQA S 5902, 5903, 5906 */

AlvBool MCU_isRamReliable(void)
{

}
