# gnu arm toolchain must be already in system path
 
import os
env = Environment(ENV = os.environ)
 
env['AR'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-ar'
env['AS'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-as'
env['CC'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-gcc'
env['CXX'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-g++'
env['LINK'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-g++'                # predefined is 'arm-none-eabi-gcc'
env['RANLIB'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-ranlib'
env['OBJCOPY'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-objcopy'
env['PROGSUFFIX'] = '.elf'
 
# include locations
env['CPPPATH'] = [
    '#Inc',
    '#Drivers/CMSIS/Include',
    '#Drivers/CMSIS/Device/ST/STM32F4xx/Include',
    '#Drivers/STM32F4xx_HAL_Driver/Inc',
    '#Drivers/STM32F4xx_HAL_Driver/Inc/Legacy',
    ]
 
# compiler flags
env.Append(CCFLAGS = [
    '-mcpu=cortex-m4',
    '-mthumb',
    '-O2',
    '-fsigned-char',
    '-ffunction-sections',
    '-fdata-sections',
    '-std=gnu11',
    '-fmessage-length=0',
    '-mthumb-interwork',
    ])
 
# linker flags
env.Append(LINKFLAGS = [
    '-ffunction-sections',
    '-fdata-sections',
    '-TTrueSTUDIO/Discovery001 Configuration/STM32F407VG_FLASH.ld',
    '-Xlinker',
    '--gc-sections',
    '--specs=nano.specs',
    ]) 
 
# defines
env.Append(CPPDEFINES = [
    'STM32F407xx',
])
 
# build everything
prg = env.Program(
    target = 'main',
    source = [
        'Src/main.c',
        'Src/stm32f4xx_hal_msp.c',
        'Src/stm32f4xx_it.c',
        'Src/sys/startup_stm32f4xx_fromCoocox.c',
        'Drivers/CMSIS/Device/ST/STM32F4xx/Source/Templates/system_stm32f4xx.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_cortex.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_dma.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_dma_ex.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_flash.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_flash_ex.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_flash_ramfunc.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_gpio.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_pwr.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_pwr_ex.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_rcc.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_rcc_ex.c',
        'Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c',
    ]
)
 
# binary file builder
def arm_generator(source, target, env, for_signature):
    return '$OBJCOPY -O binary %s %s'%(source[0], target[0])
env.Append(BUILDERS = {
    'Objcopy': Builder(
        generator=arm_generator,
        suffix='.bin',
        src_suffix='.elf'
    )
})
 
env.Objcopy(prg)