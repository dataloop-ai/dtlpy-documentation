declare module '*.svg' {
  const content: any;
  export default content;
}

declare module '@redocly/theme' {
  export const Button: React.ComponentType<{
    size?: 'small' | 'medium' | 'large' | 'xlarge';
    variant?: 'primary' | 'secondary' | 'outlined';
    tone?: 'brand' | 'default';
    to?: string;
    children: React.ReactNode;
  }>;
}

declare module '@redocly/theme/markdoc/components/Cards/Card' {
  export const Card: React.ComponentType<{
    title: string;
    to: string;
    icon?: string;
    children: React.ReactNode;
  }>;
}

declare module '@redocly/theme/markdoc/components/Cards/Cards' {
  export const Cards: React.ComponentType<{
    children: React.ReactNode;
  }>;
} 