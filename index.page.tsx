import React from "react";
import styled from "styled-components";
import tutorialsIcon from "./assets/site/icons/tutorials.svg";
import onboardingIcon from "./assets/site/icons/onboarding.svg";
import resourcesIcon from "./assets/site/icons/resources.svg";
import { ArrowRightIcon, Button } from "@redocly/theme";

const Container = styled.div`
    padding: 2rem;
`;

const Header = styled.div`
    text-align: center;
    margin-bottom: 3rem;
`;

const Title = styled.h1`
    font-size: 2.5rem;
    margin-bottom: 1rem;
`;

const Subtitle = styled.h2`
    font-size: 1.5rem;
    font-weight: normal;
    margin-bottom: 2rem;
`;

const CardSection = styled.section`
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    text-decoration: none;
    color: inherit;
    cursor: pointer;
    transition: transform 0.2s;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    margin-bottom: 1rem;
    background: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);

    &:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
`;

const DlCard = styled.div`
    text-align: center;
    max-width: 300px;

    h3 {
        margin: 0.5rem 0;
    }
`;

const CardIcon = styled.div`
    margin-bottom: 0.5rem;
    
    img {
        width: 256px;
        height: 256px;
    }
`;

const CardLink = styled.a`
    text-decoration: none;
    color: inherit;
    display: block;
    max-width: 400px;
    margin: 0 auto;
`;

const CardsContainer = styled.div`
    display: flex;
    flex-direction: row;
    gap: 1rem;
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
`;

export default function HomePage() {
    return (
        <Container>
            <Header>
                <Title>Dataloop Developers Portal</Title>
                <Subtitle>
                    A developer portal for beginners and advanced users
                </Subtitle>
                <Button
                    variant="outlined"
                    size="xlarge"
                    to="/tutorials/getting_started/sdk_overview/chapter"
                >
                    Get started <ArrowRightIcon />
                </Button>
            </Header>
            <CardsContainer>
                <CardLink href="/tutorials">
                    <CardSection>
                        <CardIcon>
                            <img src={tutorialsIcon} alt="Tutorials" />
                        </CardIcon>
                        <DlCard>
                            <h3>Tutorials</h3>
                            Step-by-step guides to get started with Dataloop
                        </DlCard>
                    </CardSection>
                </CardLink>
                <CardLink href="/onboarding/onboarding">
                    <CardSection>
                        <CardIcon>
                            <img src={onboardingIcon} alt="Onboarding" />
                        </CardIcon>
                        <DlCard>
                            <h3>Onboarding</h3>
                            Get up and running with Dataloop platform
                        </DlCard>
                    </CardSection>
                </CardLink>
                <CardLink href="/resources">
                    <CardSection>
                        <CardIcon>
                            <img src={resourcesIcon} alt="Resources" />
                        </CardIcon>
                        <DlCard>
                            <h3>Resources</h3>
                            SDKs, APIs and developer tools
                        </DlCard>
                    </CardSection>
                </CardLink>
            </CardsContainer>
        </Container>
    );
}
