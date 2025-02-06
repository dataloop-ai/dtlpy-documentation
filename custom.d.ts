declare module '*.svg' {
  const content: string;
  export default content;
}

declare module '@redocly/theme' {
  import { ReactNode } from 'react';

  export const ArrowRightIcon: React.ComponentType;
  export const Button: React.ComponentType<{
    variant?: 'primary' | 'secondary' | 'outlined';
    size?: 'small' | 'medium' | 'large' | 'xlarge';
    to?: string;
    children: ReactNode;
  }>;
}

declare module '@redocly/theme/markdoc/components/Cards/Card' {
  import { ReactNode } from 'react';
  
  export const Card: React.ComponentType<{
    title: string;
    to: string;
    icon?: string;
    children: ReactNode;
  }>;
}

declare module '@redocly/theme/markdoc/components/Cards/Cards' {
  import { ReactNode } from 'react';
  
  export const Cards: React.ComponentType<{
    children: ReactNode;
  }>;
}

declare module './@theme/components/CardWithCode/CardWithCode' {
  import { ReactNode } from 'react';
  
  export const CardWithCode: React.ComponentType<{
    title: string;
    to: string;
    icon?: string;
    children: ReactNode;
  }>;
} 