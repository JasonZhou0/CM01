/*!
 * \addtogroup MCU_COMMON MCU Common
 * \ingroup SUPPORT
 * \{
 *
 * \file     mcu_common.h
 *
 * \brief    MCU Common public interface.
 *
 * Copyright (c) 2015 Autoliv Electronics AB
 *
 * All rights reserved. Property of Autoliv Electronics AB.
 * Restricted rights to use, duplicate or disclose this code
 * are granted through contract.
 */

#ifndef MCU_COMMON_H
#define MCU_COMMON_H

/* **** Includes **** */

#include "Types.h"
#ifdef UNIT_TESTS
#include "Regsim.h"
#endif

/* **** Defines **** */

/*! Build option indicating that an option shall be included in the build. */
#define OPT_ON  1u

/*! Build option indicating that an option shall not be included in the build. */
#define OPT_OFF 0u

#define BITS_IN_ZERO_BYTES  (0u)
#define BITS_IN_ONE_BYTE    (8u)
#define BITS_IN_TWO_BYTES   (16u)
#define BITS_IN_THREE_BYTES (24u)
#define BITS_IN_FOUR_BYTES  (32u)

#define SHIFT_ZERO_BYTES    (BITS_IN_ZERO_BYTES)
#define SHIFT_ONE_BYTE      (BITS_IN_ONE_BYTE)
#define SHIFT_TWO_BYTES     (BITS_IN_TWO_BYTES)
#define SHIFT_THREE_BYTES   (BITS_IN_THREE_BYTES)
#define SHIFT_FOUR_BYTES    (BITS_IN_FOUR_BYTES)

#define BIT_0               (0u)
#define BIT_1               (1u)
#define BIT_2               (2u)
#define BIT_3               (3u)
#define BIT_4               (4u)
#define BIT_5               (5u)
#define BIT_6               (6u)
#define BIT_7               (7u)
#define BIT_8               (8u)
#define BIT_9               (9u)
#define BIT_10              (10u)
#define BIT_11              (11u)
#define BIT_12              (12u)
#define BIT_13              (13u)
#define BIT_14              (14u)
#define BIT_15              (15u)
#define BIT_16              (16u)
#define BIT_17              (17u)
#define BIT_18              (18u)
#define BIT_19              (19u)
#define BIT_20              (20u)
#define BIT_21              (21u)
#define BIT_22              (22u)
#define BIT_23              (23u)
#define BIT_24              (24u)
#define BIT_25              (25u)
#define BIT_26              (26u)
#define BIT_27              (27u)
#define BIT_28              (28u)
#define BIT_29              (29u)
#define BIT_30              (30u)
#define BIT_31              (31u)

/*! \qacexception 3412: This macro definition does not appear to expand
 *                      to a conventional expression or a recognised code construct.
 *  \qacexception 3453: A function could probably be used instead of this function-like macro.
 *                      MISRA-C:2004 Rule 19.7
 *                      Used for forced inline for performance reasons.
 *  \qacexception 3456: Parameter will be evaluated more than once when this macro is used.
 *  \qacexception 3435: Parameter occurs more than once in the replacement list of this macro.
 *                      Code review will catch incorrect usage of this macro.
 *  \qacexception 3491: Using conditional operator in a macro.
 */
/* PRQA S 3412, 3435, 3453, 3456, 3491, 4393 ++ */
#pragma PRQA_MACRO_MESSAGES_OFF "MAX", 3491
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#pragma PRQA_MACRO_MESSAGES_OFF "MIN", 3491
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#pragma PRQA_MACRO_MESSAGES_OFF "ABSDIFF", 3491
#define ABSDIFF(x, y) (((x) > (y)) ? ((x) - (y)) : ((y) - (x)))
#pragma PRQA_MACRO_MESSAGES_OFF "LIMIT_RANGE", 3412, 3435, 3456, 3491
#define LIMIT_RANGE(value, min, max) \
   do \
   { \
      (value) = MAX((value), (min)); \
      (value) = MIN((value), (max)); \
   } while (0)

/*! Get the number of array elements with return value size_t. */
#define COUNT_OF(A) (sizeof((A)) / sizeof((A)[0]))

#define IS_BIT_SET(var, bitpos) (((var) & (1uL << (bitpos))) == (1uL << (bitpos)))
#define SET_BIT(var, bitpos)    ((var) |= (1uL << (bitpos)))
#define CLEAR_BIT(var, bitpos)  ((var) &= ~(1uL << (bitpos)))

#define HTON16(var)     ((((var) & 0xFF00u) >> 8u) | (((var) & 0x00FFu) << 8u))
#define HTON32(var)     ((((var) & 0xFF000000uL) >> 24uL) | (((var) & 0x00FF0000uL) >> 8uL) | \
                         (((var) & 0x0000FF00uL) << 8uL) | (((var) & 0x000000FFuL) << 24uL))
#define NTOH16(var)     (HTON16(var))
#define NTOH32(var)     (HTON32(var))

#define UNUSED_ARG(x)   ((x) = (x))
#pragma PRQA_MACRO_MESSAGES_OFF "UNUSED_ARG_P", 3112
#define UNUSED_ARG_P(x) (void)((x) == (x))

#ifndef UNIT_TESTS
#define WRITE_HW_REG(var, val)   ((var) = (val))
#else /* #ifndef UNIT_TESTS */
#define WRITE_HW_REG(var, val)   ((var) = (val)); \
   REGSIM_monitorWatchPoint((volatile U32 *)&(var));
#endif /* #ifndef UNIT_TESTS */

#if defined(QAC)
#define WEAK_CALL(func) do {} while (0)
#elif defined(__TASKING__) || defined(__GNUC__)
#define WEAK_CALL(func) \
   do \
   { \
      void func(void) __attribute__((weak)); \
      if (func) \
      { \
         func(); \
      } \
   } while (0)
#elif defined(_MSC_VER)
#define WEAK_CALL(func) do {void func(void); func();} while (0) /* ALV S SPACING_SEMICOLON */
#else
#error Unknown compiler, check compatibility of macro
#endif

/* PRQA S 3412, 3435, 3453, 3456, 3491 -- */

/* **** Typedefs **** */

/*! Enumeration used to indicate if a function could provide its service as
    expected or if something failed. */
typedef enum
{
   MT_NOT_OK = 0,  /*!< Service failure. */
   MT_OK           /*!< Service provided as expected. */
} MT_ReturnType;

/*! Enumeration of the different safety domains. */
typedef enum
{
   MT_SD_QM = 0,  /*!< Safety domain QM. */
   MT_SD_ASIL_B   /*!< Safety domain ASIL-B. */
} MT_SafetyDomain;

/*! Voltage in millivolt. */
typedef U32 MT_Millivolt;

/*! Current in milliampere. */
typedef U32 MT_Milliampere;

/* **** Extern Variables **** */

/* **** Function Declarations **** */

#endif /* MCU_COMMON_H */
/*! \} */
